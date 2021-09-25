import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Event } from '../event.interface';

@Injectable({
  providedIn: 'root',
})
export class EventService {
  apiUrl =
    'https://rlkww3p7g8.execute-api.us-east-2.amazonaws.com/default/DC_Events_API';

  constructor(private httpClient: HttpClient) {}

  getEvents(): Observable<any> {
    return this.httpClient.get<any>(this.apiUrl);
  }
}
