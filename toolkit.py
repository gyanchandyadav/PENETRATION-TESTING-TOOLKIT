import argparse
import port_scanner, brute_forcer, subdomain_enum, dir_brute, banner_grabber

def main():
    parser = argparse.ArgumentParser(description="Modular Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    # Port scanner
    ps = subparsers.add_parser("scan", help="Scan ports")
    ps.add_argument("host")

    # SSH Brute Force
    bf = subparsers.add_parser("brute", help="SSH brute force")
    bf.add_argument("host")
    bf.add_argument("username")
    bf.add_argument("wordlist")

    # Subdomain Enumerator
    se = subparsers.add_parser("subenum", help="Enumerate subdomains")
    se.add_argument("domain")
    se.add_argument("wordlist")

    # Directory Brute Forcer
    db = subparsers.add_parser("dirbrute", help="Directory brute force")
    db.add_argument("url")
    db.add_argument("wordlist")

    # Banner Grabber
    bg = subparsers.add_parser("banner", help="Grab banner")
    bg.add_argument("host")
    bg.add_argument("port", type=int)

    args = parser.parse_args()

    if args.command == "scan":
        port_scanner.scan_ports(args.host)
    elif args.command == "brute":
        brute_forcer.ssh_brute_force(args.host, args.username, args.wordlist)
    elif args.command == "subenum":
        subdomain_enum.enumerate_subdomains(args.domain, args.wordlist)
    elif args.command == "dirbrute":
        dir_brute.dir_brute_force(args.url, args.wordlist)
    elif args.command == "banner":
        banner_grabber.grab_banner(args.host, args.port)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
