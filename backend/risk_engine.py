def assess_risk(match_result, extracted_fields=None):

    if match_result is None:

        return {

            "verification_status": "No Regulatory Alert Found.",

            "authenticity_score": 51,

            "risk_level": "Low",

            "message": "This medicine was not found in the CDSCO NSQ, Recall, or Spurious database. Based on the available regulatory data, no matching regulatory alert exists for the extracted medicine and batch.",

            "recommendation": "No regulatory alert was found for this medicine. If you have concerns about the packaging or source, verify it with your pharmacist or healthcare provider.",

            "extracted_fields": extracted_fields,

            "match_found": False,
"matched_record": None
        }

    status = str(match_result["status"]).upper()
    risk = str(match_result["risk_level"]).capitalize()

    if status == "NSQ":

        return {

            "verification_status": "Warning",

            "authenticity_score": 30,

            "risk_level": risk,

            "message": "This medicine appears in the CDSCO Not of Standard Quality (NSQ) database.",

            "recommendation": "Avoid consuming this batch until its authenticity is verified.",

            "extracted_fields": extracted_fields,

            "matched_record": match_result

        }

    elif status == "SPURIOUS":

        return {

            "verification_status": "Danger",

            "authenticity_score": 5,

            "risk_level": "Critical",

            "message": "This medicine has been reported as spurious.",

            "recommendation": "Do NOT consume this medicine. Contact your pharmacist or local drug authority immediately.",

            "extracted_fields": extracted_fields,

            "matched_record": match_result

        }

    elif status == "RECALL":

        return {

            "verification_status": "Recall",

            "authenticity_score": 10,

            "risk_level": "High",

            "message": "This medicine has been recalled.",

            "recommendation": "Stop using the medicine and return it to the seller if applicable.",

            "extracted_fields": extracted_fields,

            "matched_record": match_result

        }

    else:

        return {

            "verification_status": "Verified",

            "authenticity_score": 95,

            "risk_level": risk,

            "message": "No regulatory issues were found in the CDSCO database.",

            "recommendation": "No action is required based on the available regulatory data.",

            "extracted_fields": extracted_fields,

            "matched_record": match_result

        }


if __name__ == "__main__":

    sample_fields = {

        "drug_name": "Metronidazole IP",

        "manufacturer": "J.B. Chemicals",

        "batch_number": "BM325171",

        "expiry_date": "JUN29"

    }

    sample_match = {

        "matched_name": "Metronidazole",

        "status": "NSQ",

        "risk_level": "Moderate",

        "manufacturer": "ABC Pharma"

    }

    print(assess_risk(sample_match, sample_fields))