# Due to the way these are imported, this form of import is allowed 
from modules.instr_cls import instruct_template_cls

def get_template()->list:
    return [ instruct_template_cls(  
            name="Determine Header",
            template="""You are a helpful AI assistant. The user will provide a query, and you will choose the relevant column to search for this information:

Query: #CHUNK1
        
Available Columns: #CHUNK2 

Provide the name of the relevant column, do not add any explanations: """,
            replaceAmt=2,
            replacePrompt=["#CHUNK1","#CHUNK2"]
        ),
        ##
        instruct_template_cls(  
            name="Determine Search Query",
            template="""You are a helpful AI assistant. The user will provide a query, and you will choose what to lookup in the #CHUNK2 column:

Query: #CHUNK1
#CHUNK2 column: #CHUNK3
        
Provide the value that should be looked up, do not add any explanations: """,
            replaceAmt=3,
            replacePrompt=["#CHUNK1","#CHUNK2","#CHUNK3"]
        )
    ]        
