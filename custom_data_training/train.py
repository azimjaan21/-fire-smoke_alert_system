from ultralytics import YOLO

def train_model():
    model = YOLO('yolov8x.pt') 

    model.train(
        data=r'C:\path\to\data.yaml',
        epochs=150,                
        batch=32,                 
        imgsz=1280,                
        device='cuda',  
        lr0=0.001,     
        lr_scheduler = 'cosine',            
        weight_decay=0.001,        
        patience=10,              
        optimizer='AdamW',         
        momentum=0.9,              
        augment=True,              
        plots=True,  
        verbose=True
    )
