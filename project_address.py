class ProjectAddress:
  def __init__(self, country_code):
    self.line1 = None
    self.region = None
    self.code = None
    self.country_code = country_code

  def __str__(self):
    return f'{self.line1}, {self.code} {self.region}, {self.country_code}'
