import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { HeaderComponent } from "./components/template/header/header.component";

import { MatToolbarModule } from "@angular/material/toolbar";
import { FooterComponent } from "./components/template/footer/footer.component";
import { NavComponent } from "./components/template/nav/nav.component";

import { MatSidenavModule } from "@angular/material/sidenav";
import { MatCardModule } from "@angular/material/card";
import { MatListModule } from "@angular/material/list";
import { HomeComponent } from "./views/home/home.component";
import { EspecialidadesCrudComponent } from "./views/especialidades-crud/especialidades-crud.component";
import { EspecialidadesCreateComponent } from "./components/especialidades/especialidades-create/especialidades-create.component";
import { MatButtonModule } from "@angular/material/button";
import { MatSnackBarModule } from "@angular/material/snack-bar";
import { HttpClientModule } from "@angular/common/http";
import { FormsModule } from "@angular/forms";
import { MatFormField, MatFormFieldModule } from "@angular/material/form-field";
import { MatInputModule } from "@angular/material/input";
import { EspecialidadesReadComponent } from "./components/especialidades/especialidades-read/especialidades-read.component";
import { MatTableModule } from "@angular/material/table";
import { MatPaginatorModule } from "@angular/material/paginator";
import { MatSortModule } from "@angular/material/sort";
import { MedicoCrudComponent } from "./views/medico-crud/medico-crud.component";
import { MedicoCreateComponent } from "./components/medico/medico-create/medico-create.component";
import { MatSelectModule } from "@angular/material/select";
import { MedicoReadComponent } from "./components/medico/medico-read/medico-read.component";
import { LoginComponent } from "./account/login/login.component";
import { CreateAccountComponent } from "./account/create-account/create-account.component";
import { AuthenticationComponent } from "./views/authentication/authentication.component";
import { httpInterceptorProviders } from "./http-interceptors";
@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    NavComponent,
    HomeComponent,
    EspecialidadesCrudComponent,
    EspecialidadesCreateComponent,
    EspecialidadesReadComponent,
    MedicoCrudComponent,
    MedicoCreateComponent,
    MedicoReadComponent,
    LoginComponent,
    CreateAccountComponent,
    AuthenticationComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatCardModule,
    MatButtonModule,
    MatSnackBarModule,
    HttpClientModule,
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatTableModule,
    MatPaginatorModule,
    MatSortModule,
    MatSelectModule,
  ],
  providers: [httpInterceptorProviders],
  bootstrap: [AppComponent],
})
export class AppModule {}
