import time
import dns.resolver

# List of DNS servers to test
dns_servers = [
    "1.1.1.1",  # Cloudflare
    "8.8.8.8",  # Google Public DNS
    "9.9.9.9",  # Quad9
    # Add more DNS servers here...
]

# Domain to resolve
test_domain = "google.com"

def benchmark_dns(server):
    """
    Measures the time taken to resolve a domain using a specific DNS server.
    """

    resolver = dns.resolver.Resolver()
    resolver.nameservers = [server]

    start_time = time.time()
    try:
        resolver.resolve(test_domain)
        end_time = time.time()
        return end_time - start_time
    except dns.exception.DNSException as e:
        print(f"Error resolving with {server}: {e}")
        return None

if __name__ == "__main__":
    print("DNS Benchmark Results:")
    for server in dns_servers:
        time_taken = benchmark_dns(server)
        if time_taken:
            print(f"{server}: {time_taken:.4f} seconds")
