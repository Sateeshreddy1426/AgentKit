from flask import Flask, request, jsonify
import pandas as pd

def load_hsn_data():
    # Read first sheet
    df1 = pd.read_excel("HSN_SAC.xlsx", sheet_name=0)
    df1.columns = df1.columns.str.strip()
    df1['HSNCode'] = df1['HSNCode'].astype(str).str.strip()
    df1['Description'] = df1['Description'].astype(str).str.strip()

    # Read second sheet and rename columns to match first sheet
    df2 = pd.read_excel("HSN_SAC.xlsx", sheet_name=1)
    df2.columns = df2.columns.str.strip()
    df2 = df2.rename(columns={'SAC_CD': 'HSNCode', 'SAC_Description': 'Description'})
    df2['HSNCode'] = df2['HSNCode'].astype(str).str.strip()
    df2['Description'] = df2['Description'].astype(str).str.strip()

    # Combine dataframes and drop duplicates based on HSNCode
    df = pd.concat([df1, df2], ignore_index=True).drop_duplicates(subset='HSNCode')

    # Convert to dictionary for fast lookup
    return dict(zip(df['HSNCode'], df['Description']))

def is_valid_format(code: str) -> bool:
    # Check if code is numeric and length is 2, 4, 6, or 8
    return code.isdigit() and len(code) in [2, 4, 6, 8]

def hierarchical_check(code: str, hsn_dict: dict):
    # Return parent codes that exist in the dictionary
    levels = [code[:i] for i in [2, 4, 6, 8] if i <= len(code)]
    return {level: hsn_dict.get(level) for level in levels if hsn_dict.get(level)}

app = Flask(__name__)
hsn_dict = load_hsn_data()

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    codes = data.get('hsn_codes', [])
    result = []

    for code in codes:
        code = str(code).strip()
        if not is_valid_format(code):
            result.append({
                "code": code,
                "status": "Invalid Format",
                "message": "HSN code must be numeric and length must be 2, 4, 6, or 8"
            })
        elif code not in hsn_dict:
            result.append({
                "code": code,
                "status": "Not Found",
                "message": "HSN code not found in master data"
            })
        else:
            # Optionally include hierarchical info
            parents = hierarchical_check(code, hsn_dict)
            result.append({
                "code": code,
                "status": "Valid",
                "description": hsn_dict[code],
                "hierarchy": parents
            })

    return jsonify({"validation_result": result})

if __name__ == '__main__':
    app.run(debug=True)
