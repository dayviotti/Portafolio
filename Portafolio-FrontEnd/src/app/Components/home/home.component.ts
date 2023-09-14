import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  mostrarDiv: boolean = false;
  persona: any;
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    setTimeout(() => {
      this.mostrarDiv = true;
    }, 100);
    this.http.get('http://127.0.0.1:8000/').subscribe(data => {
      this.persona = data;
      console.log(data);
    });
  }

}
