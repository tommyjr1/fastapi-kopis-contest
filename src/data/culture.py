from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl


class JobRequest(BaseModel):
    numOfRows: Optional[int]=10  
    pageNo: Optional[int]=1  
    keyword: Optional[str]=None 

class JobResponse(BaseModel):
    title: Optional[str]=None
    description:Optional[str]=None
    subDescription:Optional[str]=None
    url:Optional[str]=None
    localId:Optional[str]=None
    issuedDate:Optional[str]=None
    createdDate:Optional[str]=None
    agent:Optional[str]=None
    temporalCoverage:Optional[str]=None
    period:Optional[str]=None

class EventRequest(BaseModel):
    numOfRows: Optional[int]=10
    pageNo: Optional[int]=1  

class EventResponse(BaseModel):
    publisher: Optional[str]=None
    collectionDb:Optional[str]=None
    creator:Optional[str]=None
    regDate:Optional[str]=None
    url:Optional[str]=None
    title:Optional[str]=None
    eventPeriod:Optional[str]=None
    rights:Optional[str]=None
    description: Optional[str]=None
    subjectCategory:Optional[str]=None
    sourceTitle:Optional[str]=None
    