import datetime


class unemployment_Job:
    def __init__(self, title, link, cnt_mthd, rslt):
        self.title = str(title)
        self.link = str(link)
        self.cnt_mthd = int(cnt_mthd)
        self.rslt = int(rslt)

    def save_job(self):
        global contacted_result
        global how_contacted
        if self.rslt == 1:
            contacted_result = "No Response"
        elif self.rslt == 2:
            contacted_result = "Return Call"
        elif self.rslt == 3:
            contacted_result = "Interview"

        if self.cnt_mthd == 1:
            how_contacted = "Website"
        elif self.cnt_mthd == 2:
            how_contacted = "Paper Application"
        elif self.cnt_mthd == 3:
            how_contacted = "Other"

        file = open("joblog.csv", "a")
        today = date.today()
        file.write("\n" + self.title + ": "
                   + "\n" + "\t" + "Web Link: " + self.link
                   + "\n" + "\t" + "Date Contacted: " + str(today)
                   + "\n" + "\t" + "Contact Method: " + how_contacted
                   + "\n" + "\t" + "Result of Contact: " + contacted_result
        )
        print("Done")
        file.close()

    def contact_info(self, person, phone):
        self.person = person
        self.phone = phone
        file = open("joblog.csv", "a")
        file.write("\n" + "\t" + self.person + " " + self.phone)
        file.close()
        print("Done")


    def new_week(self):
        dt = datetime.Now()
        start_date = datetime.datetime.strptime(str(dt), "%m/%d/%y")
        end_date = dt + datetime.timedelta(days=7)
        file = open("joblog.csv", "a")
        file.write("\n" + "Unemployment Week: " + str(start_date) + str(end_date))
        file.close()
        print("Done")

