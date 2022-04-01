

class Taxi{
    private:
        int totalDistance;

    public:
    Taxi(const char* companyName,int totalDistance);
    virtual char* getCompanyName() const;
    virtual int getFare() const;
    

};

class Bus{
    private:
    int numBoarding;

    public:
    Bus(const char* companyName,int numBoarding);
    virtual char* getCompanyName() const;
    virtual int getFare() const;


};

class Transportation{
    private:
        char companyName[10];
    
    public:
        Transportation(const char* companyName);
        virtual char* getCompanyName() const;
        virtual int getFare() const;


};

class TransportationList{
    private:
        Transportation* transportationList[50];
        int numTransportation;

    public:
        transportationList() () : numTransportation(0) {};

        void addTransportation(Transportation* const companyName) {
            transportationList[numTransportation++] = companyName; 
        }
        
        void getTotalFare() const{
            int sum = 0;
            for(int i = 0 ; i < numTransportation ; i++)
                sum += transportationList[i] ->getFare();
            
            cout << "total salary: " << sum << endl;
        }
        

        ~TransportationList();{
            for(int i = 0, i < numTransportation, i ++)
                delete transportationList[i];
        }
};



int main(void) {

TransportationList transportations; 
Transportation *pNewTransportation= NULL;
// 대중교통 이용내역 추가
pNewTransportation = new Taxi("Hongik Taxi", 1200); 
transportations.addTransportation(pNewTransportation);

pNewTransportation = new Taxi("Sangsu Taxi", 2300); 
transportations.addTransportation(pNewTransportation);

pNewTransportation = new Bus("Seogyo Bus", 130); 
transportations.addTransportation(pNewTransportation);

pNewTransportation = new Bus("Donggyo Bus", 220); 
transportations.addTransportation(pNewTransportation);

transportations.getTotalFare();
return 0; }