import { TestBed } from '@angular/core/testing';
import {
  HttpClientTestingModule,
  HttpTestingController,
} from '@angular/common/http/testing';

import { EventService } from './event.service';

import { MOCK_EVENTS } from '../mock-events';

describe('EventsService', () => {
  let eventService: EventService;
  let controller: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
    });
    eventService = TestBed.inject(EventService);
    controller = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    controller.verify();
  });

  it('mocked GET call to the API returns mock data', (done) => {
    eventService.getEvents().subscribe((response) => {
      expect(response).toEqual(MOCK_EVENTS);
      done();
    });
    const request = controller.expectOne(eventService.apiUrl);

    request.flush({ body: { Items: MOCK_EVENTS } });

    expect(request.request.method).toEqual('GET');
  });
});
