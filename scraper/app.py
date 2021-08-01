
from atlantic_council_scraper import atlantic_council_scraper
from brookings_scraper import brookings_scraper
from cap_scraper import cap_scraper
from carnegie_scraper import carnegie_scraper
from csis_scraper import csis_scraper
from heritage_scraper import heritage_scraper
from middle_east_institute_scraper import middle_east_institute_scraper
from rand_scraper import rand_scraper
import boto3


def app(dynamodb=None):
    eventList = brookings_scraper() + atlantic_council_scraper() + cap_scraper() + \
        csis_scraper() + heritage_scraper() + \
        middle_east_institute_scraper() + rand_scraper()
    # carnegie_scraper()
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', region_name='us-east-2')

    table = dynamodb.Table('DC_Events')
    for event in eventList:
        table.put_item(Item=event)


if __name__ == '__main__':
    app()
