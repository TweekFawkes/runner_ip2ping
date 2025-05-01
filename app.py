import argparse
# import socket # Removed unused import
import sys
import shutil # Add shutil import
import subprocess # Add subprocess import
import os # Add os import

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

def main():
    parser = argparse.ArgumentParser(description="Ping an IP Address using the system 'ping' command.") # Updated description
    # Use a positional argument for the IP address
    parser.add_argument('ip_address', help='IP Address to Ping') # Updated help text
    args = parser.parse_args()

    ip_address = args.ip_address

    # Basic IP format validation (optional but recommended)
    # Add more robust validation if needed (e.g., using ipaddress module)
    if '.' not in ip_address and ':' not in ip_address:
         print(f"[!] Error: '{ip_address}' does not look like a valid IPv4 or IPv6 address.", file=sys.stderr)
         return 1

    # Check if the 'ping' command is available
    ping_path = shutil.which("ping") # Check for ping
    if ping_path:
        print(f"[*] Found 'ping' executable at: {ping_path}")

        # --- List /etc contents ---
        # print("[*] Listing contents of /etc...")
        # try:
        #     etc_contents = os.listdir('/etc')
        #     for item in etc_contents:
        #         print(f"  - {item}")
        # except Exception as e:
        #     print(f"[!] Error listing /etc: {e}", file=sys.stderr)
        # print("---------------------------")
        # --- End of /etc listing ---

        # --- Check for common network configuration files ---
        # config_files = ["/etc/nsswitch.conf", "/etc/resolv.conf", "/etc/named.conf", "/etc/services"]
        # print("[*] Checking for common network configuration files...")
        # for file_path in config_files:
        #     if os.path.exists(file_path):
        #         print(f"[*] Found configuration file: {file_path}")
        #         try:
        #             with open(file_path, 'r') as f:
        #                 print(f"--- Contents of {file_path} ---")
        #                 print(f.read().strip())
        #                 print(f"------------------------------")
        #         except Exception as e:
        #             print(f"[!] Error reading {file_path}: {e}", file=sys.stderr)
        #     else:
        #         print(f"[*] Configuration file not found: {file_path}")
        # --- End of config file check ---

        # Optionally call the system 'ping' command here
        print(f"[*] Running system 'ping' command for {ip_address}...")
        try:
            # Construct the ping command with specified arguments
            ping_command = [ping_path, "-c", "3", "-D", "-n", "-O", "-v", ip_address]
            print(f"[*] Executing: {' '.join(ping_command)}") # Show the command being run
            process = subprocess.run(
                ping_command, # Use the constructed ping command
                capture_output=True,
                text=True,
                check=False, # Don't raise exception on non-zero exit code
                timeout=30 # Add a timeout (e.g., 30 seconds)
            )
            print("--- System PING Output ---") # Updated output marker
            if process.stdout:
                print("[Stdout]")
                print(process.stdout.strip())
            if process.stderr:
                print("[Stderr]")
                print(process.stderr.strip())
            if process.returncode != 0:
                print(f"[!] System 'ping' command exited with code: {process.returncode}") # Updated message
            print("---------------------------")
            # Return the exit code of the ping command itself, or 0 if successful
            return process.returncode

        except subprocess.TimeoutExpired:
             print(f"[!] Error: System 'ping' command timed out for {ip_address}", file=sys.stderr) # Updated message
             return 1 # Indicate failure
        except Exception as e:
             print(f"[!] Error running system 'ping' command: {e}", file=sys.stderr) # Updated message
             return 1 # Indicate failure

    else:
        # If ping command is not found, print error and exit
        print("[!] Error: 'ping' command not found in system PATH.", file=sys.stderr) # Updated message
        return 1 # Indicate failure

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

if __name__ == "__main__":
    # Use sys.exit() to ensure the exit code is propagated correctly
    sys.exit(main())