<h2>The Cloud Code Snippet Assignemnt Requirements</h2> 
<li>Design a Windows/Linux EC2 backup strategies using AMI</li>
<li>Research on various backup/restore strategies using AMI</li>
<li>Script the process to schedule the AMI creation</li>
<li>Script the process to use the AMI creation</li>
<li>Incorporate all the configuration changes required for the new instance to be functional</li>

The following table compares four AWS DR methods in terms of RPO, RTO and cost:
<table style="width:100%">
<tr>
    <th></th>
    <th>RTO</th> 
    <th>RPO</th>
    <th>Cost</th>
</tr>
<tr>
    <th>Backup and Restore</th>
    <td>As long as it takes to restore systems from backup</th> 
    <td>Since last backup. This depends on schedule and can be a few hours or more than a day or a week</th>
    <td>Extremely cost-effective. It depends on the retention policy. Backup can be retained for few days of a week or a month </th>
</tr>
<tr>
    <th>Pilot Light</th>
    <td>As long as it takes to detect and auto scale up replacement system</th> 
    <td>Depends on replication type</th>
    <td>Very cost-effective due to fewer 24/7 resources required</th>
</tr>
<tr>  
    <th>Fully Working Low-Capacity Standby</th>
    <td>For critical load: as long as it takes to fail over. For all other load, as long as it takes to scale further</th> 
    <td>Depends on replication type</th>
    <td>Cost saving and IT footprint samller than Multi-Site Active-Active</th>
</tr>
<tr>
    <th>Multi-Site Active-Active</th>
    <td>As long as it takes to fail over</th> 
    <td>Depends on replication type</th>
    <td>Expensive due to maintaining redundant resources</th>
</tr>
</table>

<h2>What Does This Repo Include?</h2>
This repo includes two Pythin programs as follows: 
<li>Backup: <i>ec2_to_ami.py</i> and <i>ec2_to_ami_config.py</i></li>
<li>Restore: <i>ami_to_ec2.py</i> and <i>ami_to_ec2_config.py</i></li>

<h2>What Does The Backup Program Do?</h2>
<li>The backup program includes the main script (<i>ec2_to_ami.py</i>) and the configuration module (<i>ec2_to_ami_config.py</i>)</li>
<li>The main script (<i>ec2_to_ami.py</i>) is to retrieve configuration information from the configuration module and perform backup. It also deletes old images per retention policy setting specified in the configuration module.</li>
<li>The configuration module (ec2_to_ami_config.py) is to store custom parameters such is server name, instance ID, retention policy, and etc.</li>

<h2>What Does The Restore Program Do?</h2>
<li>The restore program includes the main script (<i>ami_to_ec2.py</i>) and the configuration module (<i>ami_to_ec2_config.py</i>)</li>
<li>The main script (<i>ami_to_ec2.py</i>) is to retrieve configuration information from the configuration module and perform restore from AMIs.</li>
<li>The configuration module (<i>ec2_to_ami_config.py</i>) is to store custom parameters such as AMI ID, number of instances, instance type, and etc.</li>

<h2>Tehnical Platform</h2>
<li>AWS CLI</li>
<li>AWS SDK for Python (Boto 3)
<li>Python 2.7 and above</li>

Note that the AWS CLI tool is Python based and it shares the code base with Botocore, which is used by Boto3. As a result, it makes strategic sense to implement the solution in Python/Boto3
<h2>Useful Link</h2>

<a href="https://aws.amazon.com/sdk-for-python/">AWS SDK for Python (Boto3)</a>
<br>
<a href="https://boto3.readthedocs.io/en/latest/guide/quickstart.html">Boto 3 Quick Start</a>
<br>
<a href="https://aws.amazon.com/cli/">AWS Command Line Interface</a>
