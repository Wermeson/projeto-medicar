import { AuthGuard } from './account/shared/auth.guard';
import { CreateAccountComponent } from './account/create-account/create-account.component';
import { LoginComponent } from './account/login/login.component';
import { AuthenticationComponent } from './views/authentication/authentication.component';
import { MedicoCreateComponent } from './components/medico/medico-create/medico-create.component';
import { EspecialidadesCreateComponent } from './components/especialidades/especialidades-create/especialidades-create.component';
import { EspecialidadesCrudComponent } from './views/especialidades-crud/especialidades-crud.component';
import { HomeComponent } from './views/home/home.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MedicoCrudComponent } from './views/medico-crud/medico-crud.component';

const routes: Routes = [
  {
    path: "",
    component: HomeComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "especialidades",
    component: EspecialidadesCrudComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "especialidades/create",
    component: EspecialidadesCreateComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "medicos",
    component: MedicoCrudComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "medico/create",
    component: MedicoCreateComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "",
    component: AuthenticationComponent,
    children: [
      {path: "", redirectTo: "login", pathMatch: "full"},
      {path: "login", component: LoginComponent},
      {path: "create-account", component: CreateAccountComponent},
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
