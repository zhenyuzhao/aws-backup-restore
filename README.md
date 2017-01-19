<h2>The Cloud Code Snippet Assignemnt Requirements</h2> 
<li>Design a Windows/Linux EC2 backup strategies using AMI</li>
<li>Research on various backup/restore strategies using AMI</li>
<li>Script the process to schedule the AMI creation</li>
<li>Script the process to use the AMI creation</li>
<li>Incorporate all the configuration changes required for the new instance to be functional</li>

<h2>What Does This Repo Include?</h2>
This repo includes two Pythin programs as follows: 
<li>Backup: <i>ec2_to_ami.py</i> and <i>ec2_to_ami_config.py</i></li>
<li>Restore: <i>ami_to_ec2.py</i> and <i>ami_to_ec2_config.py</i></li>

<h2>What Does The Backup Program Do?</h2>
<li>The backup program includes the main script (<i>ec2_to_ami.py</i>) and the configuration module (<i>ec2_to_ami_config.py</i>)</li>
<li>The main script (<i>ec2_to_ami.py</i>) is to retrieve configuration information from the configuration module and perform backup. It also deletes old images per retention policy setting specified in the configuration module</li>
<li>The configuration module (ec2_to_ami_config.py) is to store custom parameters such is server name, instance ID and retention policy</li>

<h2>What Does The Restore Program Do?</h2>
<li>The restore program includes the main script (<i>ami_to_ec2.py</i>) and the configuration module (<i>ami_to_ec2_config.py</i>)</li>
<li>The main script (<i>ami_to_ec2.py</i>) is to retrieve configuration information from the configuration module and perform restore from AMIs</li>
<li>The configuration module (<i>ec2_to_ami_config.py</i>) is to store custom parameters such as AMI ID, number of instances, and instance type</li>

<h2>Useful Link</h2>

<a href="https://aws.amazon.com/sdk-for-python/">AWS SDK for Python (Boto3)</a>
<br>
<a href="https://boto3.readthedocs.io/en/latest/guide/quickstart.html">Boto 3 Quick Start</a>
<br>
<a href="https://aws.amazon.com/cli/">AWS Command Line Interface</a>
