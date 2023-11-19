# flake8: noqa
NASA_SEARCH_PROMPT = """
    This tool is a wrapper around NASA's search API, useful when you need to search through NASA's Image and Video Library. 
    The input to this tool is a query specified by the user, and will be passed into NASA's `search` function.
    
    At least one parameter must be provided.

    There are optional paramaters that can be passed by the user based on their query
    specifications.  Each item in this list contains pound sign (#) separated values, the first value is the parameter name, 
    the second value is the datatype and the third value is the description: {{

        - q#string#Free text search terms to compare to all indexed metadata.
        - center#string#NASA center which published the media.
        - description#string#Terms to search for in “Description” fields.
        - description_508#string#Terms to search for in “508 Description” fields.
        - keywords #string#Terms to search for in “Keywords” fields. Separate multiple values with commas.
        - location #string#Terms to search for in “Location” fields.
        - media_type#string#Media types to restrict the search to. Available types: [“image”,“video”, “audio”]. Separate multiple values with commas.
        - nasa_id #string#The media asset’s NASA ID.
        - page#integer#Page number, starting at 1, of results to get.-
        - page_size#integer#Number of results per page. Default: 100.
        - photographer#string#The primary photographer’s name.
        - secondary_creator#string#A secondary photographer/videographer’s name.
        - title #string#Terms to search for in “Title” fields.
        - year_start#string#The start year for results. Format: YYYY.
        - year_end #string#The end year for results. Format: YYYY.

    }}
    
    Below are several task descriptions along with their respective input examples.
    Task: get the 2nd page of image and video content starting from the year 2002 to 2010
    Example Input: {{"year_start":  "2002", "year_end":  "2010", "page": 2}}
    
    Task: get the image and video content of saturn photographed by John Appleseed
    Example Input: {{"q": "saturn", "photographer": "John Appleseed"}}
    
    Task: search for Meteor Showers with description "Search Description" with media type image
    Example Input: {{"q": "Meteor Shower", "description": "Search Description", "media_type": "image"}}
    
    Task: get the image and video content from year 2008 to 2010 from Kennedy Center
    Example Input: {{"year_start":  "2002", "year_end":  "2010", "location": "Kennedy Center}}
    """

NASA_ASSET_PROMPT = """
    This tool is a wrapper around NASA's media asset manifest API, useful when you need to retrieve a media 
    assets manifest. The input is the NASA ID of the media asset.

    For example, if you want to retrieve the manifest of a media asset, you would pass in the following dictionary:
    {{
        "nasa_id": "as11-40-5874"
    }}
    This will return asset manifest results in the form of Collection+JSON file.
"""

NASA_METADATA_PROMPT = """
    This tool is a wrapper around NASA's media asset metadata location API. Useful when you need to 
    access the media assets metadata. It provides the location to access this metadata. The input 
    is the NASA ID of the media asset. 

    For example, if you want to retrieve the location of the media assets metadata, create a similair 
    request as the following:
    {{
        "nasa_id": "as11-40-5874"
    }}
    This will return a JSON file at the location specified by the reponse to access the media assets metadata. 
"""

NASA_CAPTIONS_PROMPT = """
    This tool is a wrapper around NASA's video assests caption location API, useful when you need 
    to retrieve the location of the captions of a specific video. The input is the NASA ID of the 
    video asset.

    For example, if you want to retrieve the captions of a video, create a similar request as the 
    following: 
    {{
        "nasa_id": "172_ISS-Slosh.sr"
    }} 
    This will return a SRT or VTT file at the location specified by the response to access the videos captions. 
"""

