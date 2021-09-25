export interface Event {
  entity: string;
  entityType: string;
  dateTime: string;
  unixTimeStamp: number;
  title: string;
  link: string;
  uuid: string;
  type: string;
  additionalInfo: string | null;
}
