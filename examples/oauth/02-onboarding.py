from mollie.api.error import Error


def main(client):
    try:

        # https://docs.mollie.com/reference/v2/onboarding-api/get-onboarding-status

        body = "<h1>Get onboarding status</h1>"
        onboarding = client.onboarding.get("me")
        body += f"Status: <b>{onboarding.name}, onboarding status = {onboarding.status}</b>"

        # https://docs.mollie.com/reference/v2/onboarding-api/submit-onboarding-data

        body += "<h1>Submit onboarding data</h1>"
        data = {"profile": {"categoryCode": "6012"}}
        result = client.onboarding.create(data)
        body += str(result)

        return body

    except Error as err:
        return f"API call failed: {err}"
