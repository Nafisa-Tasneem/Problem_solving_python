
emails = ["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]
email_set = set()
for elements in emails:
    local, domain = elements.split('@')
    # print(local, domain)
    # local_str = ''
    if '+' in local:
        local_str, removed_portion = local.split('+',1)
        local = local_str
    # local_str.replace('.','')
    final_element = local.replace('.','') +'@'+ domain
    # print(final_element)
    email_set.add(final_element)
print(len(email_set))





