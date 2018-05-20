import com.sun.tools.corba.se.idl.IncludeGen;

/*********
 *
 * Minimum Word Break
 *
 * Given a string s, break s such that every substring of the partition can be found in the dictionary. Return the
 * minimum break needed.
 *
 * Examples:
 *
 * Given a dictionary ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
 *
 * input: pattern "CatMat"
 * output: 1
 * explanation: We can break the sentences
 * in three ways, as follows:
 * CatMat = [ Cat Mat ] break 1
 * CatMat = [ Ca tM at ] break 2
 * CatMat = [ C at Mat ] break 2 so the out put is: 1
 *
 * Input: DogCat
 * output: 1
 *
 * solution of this problem is based on the WordBreak Trie solution are level ordered graph. We start traversing given
 * pattern and start finding a character in a trie. If we reach a node (leaf) of a trie from where we can traverse a
 * new words of a trie (dictionary), we increment level by one and call search function for rest of the pattern
 * character in trie. In the end, we return minimum Break.
 *
 * MinBreak(Trie, key, level, start = 0)
 *      If start == key.length()
 *          update min_break
 * for i = start to keylength
 *      If we found a leaf node in trie
 *          MinBreak(Trie, key, level+1, i)
 *
 ********/

// Java program to find minimum breaks needed to break a string in dictionary words.
public class Trie {
    TrieNode root = new TrieNode();
    int minWordBreak = Integer.MAX_VALUE;

    // Trie node
    class TrieNode {
        boolean endOfTree;
        TrieNode children[] = new TrieNode[26];
        TrieNode(){
            endOfTree = false;
            for (int i=0; i<26; i++)
            {
                children[i] = null;
            }
        }
    }

    // If not present, inserts key into trie, If the key is prefix of the trie node, just marks leaf node
    void insert(String key){
        int length = key.length();

        int index;

        TrieNode pcrawl = root;

        for (int i=0; i<length; i++){
            index = key.charAt(i) - 'a';

            if (pcrawl.children[index] == null){
                pcrawl.children[index] = new TrieNode();
            }
            pcrawl = pcrawl.children[index];
        }

        // mark last node as leaf
        pcrawl.endOfTree = true;
    }

    // function break the string into minimum cut such the every substring after breaking in the dictionary.
    void minWordBreak(String key)
    {
        minWordBreak = Integer.MAX_VALUE;

        minWordBreakUtil(root, key, 0, Integer.MAX_VALUE, 0);
    }

    void minWordBreakUtil(TrieNode node, String key, int start, int min_Break, int level)
    {
        TrieNode pCrawl = node;

        // base case, update minimum break
        if (start == key.length()){
            min_Break = Math.min(min_Break, level - 1);
            if (min_Break < minWordBreak){
                minWordBreak = min_Break;
            }
            return;
        }

        // traverse given key (pattern)
        for (int i = start; i < key.length(); i++) {
            int index = key.charAt(i) - 'a';
            if (pCrawl.children[index] == null) {
                return;
            }

            // If we find a condition were we can move to the next word in a trie dictionary
            if (pCrawl.children[index].endOfTree) {
                minWordBreakUtil(root, key, i+1, min_Break, level+1);
            }
            pCrawl = pCrawl.children[index];
        }
    }

    public static void main(String[] args)
    {
        String keys[] = {"cat", "mat", "ca", "ma", "at", "c", "dog", "og", "do"};

        Trie trie = new Trie();

        // construct trie

        int i;
        for (i=0; i<keys.length; i++){
            trie.insert(keys[i]);
        }

        trie.minWordBreak("catmatat");
        System.out.println(trie.minWordBreak);
    }
}