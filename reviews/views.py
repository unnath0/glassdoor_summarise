from django.shortcuts import render

# Create your views here.
def search(request):
    company_name = request.GET.get('company_name')
    
    # TODO: search the matching companies from glassdoor
    companies = ['Company A', 'Company B', 'Company C', 'Company D']
    #companies = []

    context = {
            'companies': companies
    }

    return render(request, 'search.html', context)

def review(request, company):
    # TODO: scrape glassdoor to get reviews for the company
    # TODO: send the reviews to gemini ai to summarise

    overall_review = """
        Pros

            good work life balance .

        Cons

            salary not up to market standards no benefits poor management not interesting projects
    """

    context = {
            'company_name': company,
            'overall_review': overall_review
    }
    return render(request, 'review.html', context)
