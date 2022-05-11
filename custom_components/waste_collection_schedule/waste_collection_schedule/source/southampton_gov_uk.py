import requests
from waste_collection_schedule import Collection  # type: ignore[attr-defined]
from waste_collection_schedule.service.ICS import ICS

TITLE = "Southampton.gov.uk"
DESCRIPTION = "Source for Southampton.gov.uk city council waste services in the city of Southampton, UK."
URL = "https://www.southampton.gov.uk"
TEST_CASES = {
    "Zabelweg 1B": {"hnId": 53814},
}


class Source:
    def __init__(self, uprn):
        self._uprn = uprn
        self._ics = ICS()

    def fetch(self):
        files = {
            "ufprt": (
                None,
                "8889BD7ABF8822E7BA24F32217C7CD5A667E9545ACF1DED9BBD44EFED2A0E8CDB6D80A49FD1094D8D928A4AE4B0F989FAAE5FC51300356F39C18EB4201DB8C6DB57F297B3129D4D1D049195CC2C2A77567F3B4C03B48872D7FB8787B0B4F77C44E0316622D54C717BD54BD40E7DDEE568C996E08B039AD6057A0C0DB5E15E7B27E2C4B1B9DBF7299793C38AA6A70D0BF072AE77CF5FE3977352EAC7773F7095788194EEA531DE44FCB81C491203C969B",
            )
        }
        # get ics file
        r = requests.post(
            "https://www.southampton.gov.uk/whereilive/waste-calendar/?UPRN="
            + str(self._uprn),
            files=files,
        )

        dates = self._ics.convert(r.text)

        entries = []
        for d in dates:
            entries.append(Collection(d[0], d[1].lower().capitalize()))
        return entries
