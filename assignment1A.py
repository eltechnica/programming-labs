def your_url():
    print("Let's make a website" + "!")
    
    scheme = input("Scheme: ")
    subdomain = input("Subdomain: ")
    second_level_domain = input("Second-level Domain: ")
    top_level_domain = input("Top Level Domain: ")
    subdirectory = input("Subdirectory: ")

    url = f"{scheme}://{subdomain}.{second_level_domain}.{top_level_domain}/{subdirectory}"

    print("Your URL is: " + url)

# Call the function
your_url()
