This is a test
**************
:init:

Initialises a workflow by attempting to save a non-template workflow to the database.
It will retrieve workflow template information for the workflow name and populate the new workflow with the information. It will also populate these workflow fields with initial default values: current_step_task, template_id, status, state.

**Parameters:**    
    * **name** - the name of a workflow as a string.
    
    i.e. send a JSON request in this format:

    ::

        {
            "name": unicode(50)
        }
    
**Returns:**
    Inside the JSON response dict:
        * **errors** - a list of any errors (strings) that may have occurred.
        * **confirmations** - a list of any confirmations that may have occurred.
        * **workflow_id** - the ObjectId string of the new workflow.
    e.g.
    
    ::
    
        {
            "errors": [],
            "confirmations: ["Successfully initialised workflow. "]
            "workflow_id": "4ea5e2afcd8bbf1491000005"
        }
        
**Usage example:**

::

    base_url = "http://asapweb3.local.org.nz:9003/approvals/"
    request_dic = {"name": "Purchase Order Workflow}
    req = urllib2.Request(url=base_url + "init", 
                          data=json.dumps(request_dic),
                          headers={"Content-Type": "application/json"}
                        )
    opener = urllib2.build_opener()
    resp = opener.open(req)
    json_resp_strg = resp.read()
    # Get the info from the json string
    json_resp = json.loads(json_resp_strg)        

