
from atlantic_council_scraper import atlantic_council_scraper
from brookings_scraper import brookings_scraper
from cap_scraper import cap_scraper
from carnegie_scraper import carnegie_scraper
from csis_scraper import csis_scraper
from heritage_scraper import heritage_scraper
from middle_east_institute_scraper import middle_east_institute_scraper
from rand_scraper import rand_scraper

eventList = brookings_scraper() + atlantic_council_scraper() + cap_scraper() + \
    csis_scraper() + heritage_scraper() + \
    middle_east_institute_scraper() + rand_scraper()
# carnegie_scraper()

print(eventList)
