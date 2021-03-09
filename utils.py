def get_arguments():
    # This method get arguments from the console execution
    parser = optparse.OptionParser()

    # Adding options to the OptionParser object
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC Address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC Address')

    # Getting the options and arguments from the command line execution
    options, arguments = parser.parse_args()

    # Validating the obtained information
    if not options.interface:
        parser.error("[-] Please specify an interface, use python mac_changer.py --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use python mac_changer.py --help for more info.")

    # Returning the options
    return options