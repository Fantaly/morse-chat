#Enter in the morse-chat-fe folder and run npm run dev, then enter in the morse-chat-be folder and uvicorn main:app --host 0.0.0.0 --reload
cd morse-chat-fe
npm run dev & 
cd ../morse-chat-be/app
uvicorn main:app --host 0.0.0.0 --reload

