from atlantic_council_scraper import atlantic_council_scraper
from brookings_scraper import brookings_scraper
from cap_scraper import cap_scraper
from carnegie_scraper import carnegie_scraper
from csis_scraper import csis_scraper
from heritage_scraper import heritage_scraper
from middle_east_institute_scraper import middle_east_institute_scraper
from rand_scraper import rand_scraper
from wilson_center_scraper import wilson_center_scraper
from delete_table import delete_table
import boto3

# this lambda function is a cron job that runs weekly every Sunday


def lambda_handler(event, context, dynamodb=None):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    eventList = brookings_scraper() + atlantic_council_scraper() + cap_scraper() + \
        csis_scraper() + heritage_scraper() + \
        middle_east_institute_scraper() + rand_scraper() + wilson_center_scraper()
    # carnegie_scraper()
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', region_name='us-east-2')

    # delete all items in table
    delete_table("DC_Events")

    table = dynamodb.Table('DC_Events')
    eventCount = 0
    for event in eventList:
        table.put_item(Item=event)
        eventCount += 1
        if (eventCount >= 100):
            break
