import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class EventService {
  apiUrl =
    'https://rlkww3p7g8.execute-api.us-east-2.amazonaws.com/default/DC_Events_API';

  constructor(private httpClient: HttpClient) {}

  getEvents(): Observable<any> {
    return this.httpClient
      .get<any>(this.apiUrl)
      .pipe(map((response) => (response = response.body.Items)));
  }
}
