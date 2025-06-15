from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
import traceback
from main import run_audit_pipeline
from io import StringIO

router = APIRouter()

@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode()))
        df.to_csv("email_list.csv", index=False)

        result = run_audit_pipeline()

        if not isinstance(result, dict):
            result = {"message": "Audit complete, but result not in dictionary format."}

        # Optional: Add issue count summary
        issue_count = len(result.get("issues", []))
        result["issue_summary"] = f"{issue_count} issues found."

        return JSONResponse(content=result)

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=400, content={"error": str(e)})
