import logging
logging.basicConfig(
    filename='trace_env_day2.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

expected_cluster_roles={"namenode","datanode","resourcemanager","nodemanager","hiveserver2"}
user_input=input("Enter cluster roles, comma separated:")
roles_present=set(role.strip().lower() for role in user_input.split(","))
missing_roles= expected_cluster_roles - roles_present

print("Roles Present:",roles_present)


if missing_roles:
    print("Missing Roles List:",missing_roles)
    logging.warning(f"Missing Services in this cluster, Need to add services:{missing_roles}")
else:
    print("All Service Roles present: Cluster healthy")
    logging.info(f"Cluster is healthy- All Roles present")





