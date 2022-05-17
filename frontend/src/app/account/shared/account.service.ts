import { MatSnackBar } from '@angular/material/snack-bar';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AccountService {
  loginUrl = 'http://127.0.0.1:8000/login/'
  createUserUrl = 'http://127.0.0.1:8000/users/'
  constructor(private http: HttpClient, private snackBar: MatSnackBar) { }

  async login(user: any) {
    const result = await this.http.post<any>(this.loginUrl, user).toPromise();
    console.log(result)
    if (result && result.token) {
      window.localStorage.setItem('token', result.token);
      return true;
    }

    return false;
  }

  async createAccount(account: any) {
    const result = await this.http.post<any>(this.createUserUrl, account).toPromise();
    return result;
  }

  showMessage(msg: string, isError: boolean = false): void {
    this.snackBar.open(msg, 'X', {
      duration: 3000,
      horizontalPosition: "right",
      verticalPosition: "top",
      panelClass: isError ? ['msg-error'] : ['msg-success']
    })
  }

  getAuthorizationToken() {
    const token = window.localStorage.getItem('token');
    return token;
  }

  // getTokenExpirationDate(token: string): Date {
  //   const decoded: any = jwt_decode(token);

  //   if (decoded.exp === undefined) {
  //     return null as any;
  //   }

  //   const date = new Date(0);
  //   date.setUTCSeconds(decoded.exp);
  //   return date;
  // }

  // isTokenExpired(token?: string): boolean {
  //   if (!token) {
  //     return true;
  //   }

  //   const date = this.getTokenExpirationDate(token);
  //   if (date === undefined) {
  //     return false;
  //   }

  //   return !(date.valueOf() > new Date().valueOf());
  // }

  // isUserLoggedIn() {
  //   const token = this.getAuthorizationToken();
  //   if (!token) {
  //     return false;
  //   } else if (this.isTokenExpired(token)) {
  //     return false;
  //   }

  //   return true;
  // }
}
