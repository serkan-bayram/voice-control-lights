# A Program To Control Your Tapo Lights With Voice Commands

### Step 1: Open your Tapo app and click **Me**.

<img width="284" alt="image" src="https://user-images.githubusercontent.com/68502470/213877669-8a88f62d-9b0c-4f87-81a6-fdf0749936b5.png">

### Step 2: Click **Third-Party Services** and click **IFTTT**. Follow the instructions and connect your TAPO account to IFTTT.

![image](https://user-images.githubusercontent.com/68502470/213877686-31945f01-0aab-414d-9ae8-321330e8b3b9.png)
![image](https://user-images.githubusercontent.com/68502470/213877699-87912a4d-0f4c-4521-8397-b24626d5b5da.png)
![image](https://user-images.githubusercontent.com/68502470/213877710-efa956d8-c539-4ee6-9d4e-5b746baa743b.png)

### Step 3: Go to **https://ifttt.com/create**.

### Step 4: Click **If This**, search for **Webhooks** and choose it.

![image](https://user-images.githubusercontent.com/68502470/213877283-dba1ea99-b369-4142-a022-185995533230.png)

### Step 5: Click **Receive a web request**, enter an event name and click **Create trigger**. My event names are **bulb_on** and **bulb_off**. If you enter different name you have to modify it in the code.

![image](https://user-images.githubusercontent.com/68502470/213877306-73efbe51-fa3a-4c3a-a592-43468dd36317.png)
![image](https://user-images.githubusercontent.com/68502470/213877336-220e14a5-3286-4ed7-9f90-e95de6e39432.png)

### Step 6: Click **Then That**, search for **TP-LINK Tapo**, these are the actions you can choose. You can modify the code according to the action.

![image](https://user-images.githubusercontent.com/68502470/213877351-22205f82-1573-438e-8fdd-38158bedec42.png)
![image](https://user-images.githubusercontent.com/68502470/213877375-bf20110b-45ca-465c-8fd2-273b0c47bee9.png)

### Step 7: Click **Turn On**, choose TP-Link Tapo account and device, click **Create action**, click **Continue**, click **Finish**. 

![image](https://user-images.githubusercontent.com/68502470/213877389-f42e5014-9639-4cb8-8ab6-0b9cfa9be025.png)

### Step 8: Now your IFTTT action is ready for the turn lights on but we need an API key to make it work.

<img width="1055" alt="image" src="https://user-images.githubusercontent.com/68502470/213877435-8533eba0-5826-4996-8baf-b895d545f2fc.png">

### Step 9: Go to **https://ifttt.com/maker_webhooks** and click **Documentation**. Save your key in a txt file called **key.txt**.

![image](https://user-images.githubusercontent.com/68502470/213877473-8fcce2d8-b97e-468c-aad8-c26a64d428a4.png)

### Step 10: Repeat the instructions for "Turn Off" action.
