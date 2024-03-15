/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if (list1==NULL && list2==NULL) return NULL;
    else if (list1==NULL) return list2;
    else if (list2==NULL) return list1;
    else
    {
        struct ListNode *ans,*head;
        if (list1->val<list2->val)
        {
            ans=list1;
            list1=list1->next;
        }
        else
        {
            ans=list2;
            list2=list2->next;
        }
        head=ans;
        while (list1!=NULL && list2!=NULL)
        {
            if (list1->val<list2->val)
            {
                head->next=list1;
                list1=list1->next;
            }
            else
            {
                head->next=list2;
                list2=list2->next;
            }
            head=head->next;
        }
        if (list1!=NULL) head->next=list1;
        else head->next=list2;
        return ans;  
    }
    
}