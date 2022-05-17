import { Observable } from "rxjs";
import { Medico } from "./medico.model";
import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { MatSnackBar } from "@angular/material/snack-bar";

@Injectable({
  providedIn: "root",
})
export class MedicoService {
  baseUrl = "http://127.0.0.1:8000/medicos/";

  constructor(private snackBar: MatSnackBar, private http: HttpClient) {}

  showMessage(msg: string, isError: boolean = false): void {
    this.snackBar.open(msg, "X", {
      duration: 3000,
      horizontalPosition: "right",
      verticalPosition: "top",
      panelClass: isError ? ["msg-error"] : ["msg-success"],
    });
  }

  create(medico: Medico): Observable<Medico> {
    // var token = "4092f2783bdd727b97dd24cf2ff21aa9cab065cc";
    // const headers = new HttpHeaders().set('Authorization', `bearer ${token}`);
    return this.http.post<Medico>(this.baseUrl, medico);
  }

  read(): Observable<Medico[]> {
    return this.http.get<Medico[]>(this.baseUrl);
  }
}
