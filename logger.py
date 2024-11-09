import logging
import os
import sys
from tkinter import messagebox

# Create the logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure the logger
logging.basicConfig(
    filename="logs/error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Create a logger named after this module for easier tracking in multi-module apps
logger = logging.getLogger(__name__)


def handle_exception(exc_type, exc_value, exc_traceback):
    """Handle all uncaught exceptions and log them."""
    # Log the error to the log file
    logger.error("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))
    
    # Show a messagebox for the error
    messagebox.showerror("Error", "An unexpected error occurred. Please check the error log.")

# Attach the handler to Tkinter and the global exception hook
sys.excepthook = handle_exception  # For non-Tkinter exceptions

def tk_handle_exception(exc_type, exc_value, exc_traceback):
    """Tkinter-specific exception handler."""
    handle_exception(exc_type, exc_value, exc_traceback)  # Delegate to the main exception handler
