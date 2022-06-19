int Yp = 450;

void setupCreditos() {
  Yp = 450;
}

void creditos() {
  
  background(255);
  strokeWeight(4);
  stroke(70,139,30);
  fill(99,166,61);
  rectMode(CENTER);
  
  //Faz a animação do Texto subir
   
  if (Yp>150) {
    Yp--;
  }
    
  background(255);
  fill(0);
  textSize(48);
  textAlign(CENTER, CENTER);
  text("Créditos",width/2,70);
  textSize(24);
  text("Leandro de Carvalho Medeiros",width/2,Yp);
  text("Yan Felipe Ferreira da Silva", width/2,Yp+30);
  text("Leonardo Alves dos Santos",width/2,Yp+60);
  text("Luca Takemura Piccoli",width/2,Yp+90);
  text("Rafael da Silva Albuquerque",width/2,Yp+120);
  
  if (mouseX > 100 - 78 && mouseX < 100 + 78 && mouseY > 32 - 18 && mouseY < 32 + 18){
    mouseOver = 1;
  }
  else {
    mouseOver = 0;
  }
    
  //trocar o botão de cor
  if (mouseOver == 1) {
    fill(70,139,30); 
  } 
  else {
    fill(99,166,61);
  }
  rect(100, 32, 156, 36);

  //Textos
  fill(0);
  textSize(28);
  textAlign(CENTER, CENTER);
  text("Voltar", 100, 28);
}

void mousePressedCreditos() {
  if (mouseOver == 1) {
    currState = 0;
  }
}
