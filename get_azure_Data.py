from tfs import TFSAPI
from datetime import datetime

class AzureData:

    def __init__(self, org_url, personal_access_token, project):
        self.project = project
        self.org_url = org_url
        self.personal_access_token = personal_access_token
        self.client = TFSAPI(org_url, pat=personal_access_token)
        print("azure connected...")

    def get_close_workitem(self, today=datetime.today().strftime('%Y-%m-%d')):
        query = f"select System.Id from workitems WHERE [System.TeamProject] = '{self.project}' " \
                f"And [System.State] = 'Closed' And [System.WorkItemType] <> 'Task' And [Microsoft.VSTS.Common.StateChangeDate] = '{today}'"
        workitems = self.client.run_wiql(query).workitems  # runs a query and fetch workitems
        rows = []
        for workitem in workitems:
            row = [
                workitem['system.Id'],
                workitem["System.WorkItemType"],
                workitem['System.State'],
                workitem['System.AssignedTo'][:workitem['System.AssignedTo'].find('<') - 1].replace('.', ' ').title() if workitem['System.AssignedTo'] else 'N\\A',
                workitem["System.CreatedDate"],
                workitem['Microsoft.VSTS.Common.StateChangeDate'],
                workitem["System.Title"],
            ]
            rows.append(row)
        return rows
