from django.db import models

# Create your models here.
class Account(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    AliasName = models.CharField(max_length=255)
    AccoutID = models.CharField(max_length=20)

class AccountMember(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    AccountMemberID = models.CharField(max_length=20)

class BillingAccount(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    BillingAccID = models.CharField(max_length=20)

class Invoice(models.Model):
    InvoiceNumber = models.CharField(max_length=20)
    BAccName = models.CharField(max_length=255)
    BillingAddress = models.CharField(max_length=255)

class AccountAdmin(models.Model):
    AccountAdminID = models.CharField(max_length=20)
    LastName = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)

class Associate(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Role = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    AssociateID = models.CharField(max_length=20)

class Customer(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    CustomerID = models.CharField(max_length=20)
    Alias = models.CharField(max_length=255)
    RiskInformationURL = models.CharField(max_length=255)

class CustomerRelationship(models.Model):
    CustomerA = models.CharField(max_length=20)
    CustomerB = models.CharField(max_length=20)
    relationship = models.CharField(max_length=255)

class Contract(models.Model):
    ContractNumber = models.CharField(max_length=20)
    PlanName = models.CharField(max_length=255)
    SeriesName = models.CharField(max_length=255)
    LineOfBusiness = models.CharField(max_length=255)

class ContractBenefit(models.Model):
    ContractNumber = models.CharField(max_length=20) 
    PolicyCountContribution = models.CharField(max_length=255)

class ContractPremium(models.Model):
    PremiumCode = models.CharField(max_length=20)
    AnnualizePremium = models.CharField(max_length=255)

class Product(models.Model):
    PlanName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    AnnualizePremium = models.CharField(max_length=255)

class ManagerContract(models.Model):
    SitCode = models.CharField(max_length=20)
    CompanyCode = models.CharField(max_length=20)
    WritingNumber = models.CharField(max_length=20)
    Level = models.CharField(max_length=255)
    IssueDate = models.CharField(max_length=255)

class ProductContract(models.Model):
    PlanName = models.CharField(max_length=255)
    ContractNumber = models.CharField(max_length=20)
    RiskLevel = models.IntegerField()
    AnnualizePremium = models.IntegerField()

class BenefitPremium(models.Model):
    ContractNumber = models.CharField(max_length=20)
    PremiumCode = models.CharField(max_length=20)

class CustomerCustomer(models.Model):
    CustomerA = models.CharField(max_length=20)
    CustomerB = models.CharField(max_length=20)

class CustomerBenefit(models.Model):
    CustomerID = models.CharField(max_length=20)
    ContractNumber = models.CharField(max_length=20)

class CustomerContract(models.Model):
    Price = models.CharField(max_length=20)
    RiskLevel = models.CharField(max_length=20)
    CustomerID = models.CharField(max_length=20)
    ContractNumber = models.CharField(max_length=20)

class ManagerAssociate(models.Model):
    SitCode = models.CharField(max_length=20)
    AssociateID = models.CharField(max_length=20)

class ManagerAccount(models.Model):
    SitCode = models.CharField(max_length=20)
    AccountID = models.CharField(max_length=20)

class AccountAccAdmin(models.Model):
    AccountID = models.CharField(max_length=20)
    AccountAdminID = models.CharField(max_length=20)

class AccountBillingAcc(models.Model):
    AccountID = models.CharField(max_length=20)
    BillingAccountID = models.CharField(max_length=20)

class BillingAccountInvoice(models.Model):
    BillingAccountID = models.CharField(max_length=20)
    InvoiceNumber = models.CharField(max_length=20)

class AccountAccMember(models.Model):
    AccountID = models.CharField(max_length=20)
    AccountMemberID = models.CharField(max_length=20)

class AccountCustomer(models.Model):
    AccountID = models.CharField(max_length=20)
    CustomerID = models.CharField(max_length=20)

class CustomerAssociate(models.Model):
    CustomerID = models.CharField(max_length=20)
    AssociateID = models.CharField(max_length=20)