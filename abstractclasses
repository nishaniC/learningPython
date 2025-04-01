import abc
class scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass
    @abc.abstractmethod
    def get_scanner_status(self):
        pass
    
    
class printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass
    @abc.abstractmethod
    def get_printer_status(self):
        pass
    
class MFD1(scanner,printer):
    def scan_document(self):
        return "document has been scanned"
        
    def get_scanner_status(self):
        status={'maxResolution': 20, 'serialnumber':101}
        return status
         
    def print_document(self):
        return "document printed"
    
    def get_printer_status(self):
        status={'maxResolution': 30, 'serialnumber':102}
        return status
        
class MFD2(scanner,printer):
    def __init__(self):
        self.scanned=0
        self.printed=0
        
    def scan_document(self):
        self.scanned+=1
        return "document has been scanned"
        
    def get_scanner_status(self):
        status={'maxResolution': 220, 'serialnumber':201,'scanneDocs':self.scanned }
        return status
         
    def print_document(self):
        self.printed+=1
        return "document printed"
    
    def get_printer_status(self):
        status={'maxResolution': 230, 'serialnumber':202,'printedDocs':self.printed}
        return status
    

        
class MFD3(scanner,printer):
    def __init__(self):
        self.scanned=0
        self.printed=0
        
    def scan_document(self):
        self.scanned+=1
        return "document has been scanned"
        
    def get_scanner_status(self):
        status={'maxResolution': 220, 'serialnumber':201, 'scanneDocs':self.scanned}
        return status
         
    def print_document(self):
        self.printed+=1
        return "document printed"
    
    def get_printer_status(self):
        status={'maxResolution': 330, 'serialnumber':303, 'printedDocs':self.printed}
        return status
    
        
MFDs=[MFD1(),MFD2(),MFD3()]

for mfd in MFDs:
    print(mfd.scan_document())
    print(mfd.print_document())
    print(mfd.get_scanner_status())
    print(mfd.get_printer_status())
    

           
         
