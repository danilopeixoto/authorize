from datetime import datetime

from pydantic import BaseModel


class Model(BaseModel):
  '''Base model with custom configuration and encoders.'''

  class Config:
    '''Base model configuration.'''

    allow_mutation = False
    allow_population_by_field_name = True

    json_encoders = {
      datetime: lambda value: value.isoformat(
        timespec = 'milliseconds').replace('+00:00', 'Z')
    }
