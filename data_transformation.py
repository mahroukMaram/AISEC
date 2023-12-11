import pandas as pd



class DataTransformer():
    def __init__(self):
        pass

    def ingest_clean(self, path):
        data=pd.read_csv(path)
        data=data.drop(columns=['Timestamp','Do you agree on sharing with us some information that we will use later on to contact you?'], errors='ignore')
        data=data[data['Age']<30]

        return data

    def transform(self, data):
        data_frames = []
        df=data['What type of internship are you interested in?'].groupby(data['What type of internship are you interested in?']).aggregate('count')
        df = df.to_frame()
        data_frames.append(df)

        for x,y in data.groupby('What type of internship are you interested in?'):
            match x:
                case 'Global Talent':
                    gta = y
                    data_frames.append(gta)
                case 'Global Teacher':
                    gte = y
                    data_frames.append(gte)
                case 'Global Volunteer':
                    gv = y
                    data_frames.append(gv)

        return data_frames
        
