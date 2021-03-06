import pytest
import sample_backend

def test_find_users_by_name_success():  
    expected = [
        {
            'id' : 'abc123',            
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222',            
            'name': 'Mac',
            'job': 'Professor',
        },        
    ]
    assert sample_backend.find_users_by_name("Mac") == expected

def test_find_users_by_name_fail():  
    expected = [] 
    assert sample_backend.find_users_by_name("Jeff") == expected

# def test_should_fail():
#     assert 2==3
