
import os
from datetime import datetime, timezone

class FinancialDataManager:
    def __init__(self, output_directory = "financial_workspace1"):
        self.base_dir = output_directory
        self.ledger_file = os.path.join(self.base_dir, "pipeline_status.log")
        os.makedirs(self.base_dir, exist_ok=True)

    def append_log(self, ticker:str, status_message:str):
        timestamp = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M:%S UTC")
        log_line = f"[{timestamp}] Ticker: {ticker} | {status_message}\n"

        try:
            with open(self.ledger_file , mode = 'a', encoding = "utf-8") as file:
                file.write(log_line)

        except OSError as e:
            print(f'[CRITICAL ERROR] Failed to Write to ledger log file:{e}')

    def stage_extracted_text(self, ticker:str, raw_text:str) -> bool:
        filename = f"{ticker}_extracted.txt".upper()
        target_path = os.path.join(self.base_dir, filename)
        self.append_log(ticker,"Attempting to stage file writing operation")

        try:
            with open(target_path, mode = 'w', encoding="utf-8") as file:
                file.write(raw_text)
            self.append_log(ticker, f"successfully staged text at:{filename}")
            print(f"\n success , staged artifact saved to {target_path}")
            return True
        
        except PermissionError:
            error_msg = f"[CRITICAL] PERMISSION DENIED WRITING TO FILE {filename}"
            print(error_msg)
            self.append_log(ticker,error_msg)
            return False

        except OSError as e:
            error_msg = f"[CRITICAL] DISK I/O ERROR OCCUREDE {filename}"
            print(error_msg)
            self.append_log(ticker,error_msg)
            return False

if __name__ == "__main__":
    manager = FinancialDataManager()

    success = manager.stage_extracted_text(
        ticker = "AB Corporation",
        raw_text="AB Corp **** Annual NetProfit: 50000Cr"
    )
    print(f"\n Program Status  {success}")

        



    