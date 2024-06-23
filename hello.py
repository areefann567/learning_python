print("hey there")
name= "MOHAMMED ARIF"
print(name.split(" ")[1])  # 0/p->ARIF
lastname= name.split(" ")[1]
print(lastname.lower())
arn="arn:partition:service:region:account-id:resource-type/resource-id"
print(arn.split("/")[1])     # 0/p->resourse-id