import jobs
"""
Example: umemployment_Job("Title", "Web Link", "Contact Method", "Result of Contact")
        Contact Method
            1: Website
            2: Paper Application
            3: Other           
        Result of Contact:
            1: No Response
            2: Return Call
            3: Interview
"""
jb = jobs.unemployment_Job("Fabricator/Assembler", "https://www.ziprecruiter.com/jobs/chipton-ross-inc-13cf6658/fabricator-assembler-01c53fb5?lvk=1pe7BpJR3D-IOI3ppI4ZMg.--MsRH13tTs#intsrc=suggested-jobs", 1, 1)
jb.new_week()
