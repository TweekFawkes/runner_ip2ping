# runner_ip2ping

This script takes an IP address as input and uses the system's `ping` command to send ICMP ECHO_REQUEST packets to the target host.

## Usage

```bash
python app.py <ip_address>
```

The script will execute the following command:

```
ping -c 3 -D -n -O -v <ip_address>
```

It requires the `ping` command to be available in the system's PATH.

The script will output:
- The location of the `ping` executable if found.
- The exact `ping` command being executed.
- The standard output and standard error from the `ping` command.
- An error message if the `ping` command is not found or if it times out or encounters an error.
- The exit code of the `ping` command itself.