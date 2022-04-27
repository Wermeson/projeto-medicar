import { Especialidade } from './especialidade.model';
import { Injectable } from '@angular/core';
import {MatSnackBar} from '@angular/material/snack-bar';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EspecialidadeService {
  baseUrl = 'http://127.0.0.1:8000'

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  showMessage(msg: string, isError: boolean = false): void {
    this.snackBar.open(msg, 'X', {
      duration: 3000,
      horizontalPosition: "right",
      verticalPosition: "top",
      panelClass: isError ? ['msg-error'] : ['msg-success']
    })
  }

  private getHeader(): HttpHeaders {
    const token = localStorage.getItem('token');
    const header = new HttpHeaders({ Authorization: `Token ${token}` });
    return header;
  }

  create(especialidade: Especialidade): Observable<Especialidade>{
    // var token = "4092f2783bdd727b97dd24cf2ff21aa9cab065cc";
    // const headers = new HttpHeaders().set('Authorization', `bearer ${token}`);
    return this.http.post<Especialidade>(this.baseUrl + '/especialidades/', especialidade)
  }

  read(): Observable<Especialidade[]>{
    return this.http.get<Especialidade[]>(this.baseUrl + '/especialidades/')
  }
}
