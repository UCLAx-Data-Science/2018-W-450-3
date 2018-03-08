# Create an EMR Cluster

1. Access the EMR Console.
2. Choose "Create Cluster".
3. Select "Go to advanced options".
4. Under Step 1: Software and Steps, leave the default options and click **Next**.
5. Under Step 2: Hardware,
   - Remove the Task Group
   - Change the Master Group and Core Group to instance type `m4.large`
   - Change the Purchasing Option to Spot with maximum spot price $0.10.
6. Under Step 3: General Cluster Settings,
   - Change the logging directory to `s3://your-bucket/logs/` (Enter the text manually)
   - Remove Debugging
   - Remove Termination Protection
   - Expand Bootstrap Actions
   - Add a Bootstrap Action >> Custom Action and click "Configure and Add"
   - Set the Script Location to `s3://awsdocs/gettingstarted/latest/sentiment/config-nltk.sh` and click **Add**.
7. Under Step 4: Security, leave the default options and click **Create Cluster**.

## Add SSH to the Master Security Group

The Security Group associated with the master node will need to have port 22 added.
